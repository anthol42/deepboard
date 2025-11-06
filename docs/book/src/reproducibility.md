# Reproducibility

In this tutorial, we’ll learn how to use the deepboard tool. Before diving in, we’ll first discuss the best practices 
for using it effectively. Since the main purpose of deepboard is to ensure the reproducibility of previously run and 
reported experiments, adopting a few coding habits will help you make full use of its features.

## Deterministic philosophy
The main idea is that an experiment with the same configuration should always run the same code. For example, let's say 
we first run a baseline experiment and get some results. Then, we can add a new feature that improves our performances 
... or degrades them. In the last  case, we might want to revert back to the previous version of the code. If we 
naively implemented the new feature to always run, we would not be able to reproduce the previous results. Of course, 
we could comment out the new feature, but this does not scale well when we have many features to try. Instead, we 
should implement the new feature in an optional fashion, and activate it when a certain parameter is set. For example, 
we could test the new feature when passing a flag to our program with a command line argument. When the flag is not 
present, we run our baseline code.

Let's look at a simple code example:

*main.py* — Baseline implementation :
```python
def experiment():
    # We start by loading the data.
    data = load_data()
    # Then, we create the model.
    model = Model()
    # Finally, we train and evaluate the model.
    return train_and_evaluate(model, data)
```
Run it with:
```bash
python main.py
```

Next, we implement a new feature that will be activated when passing a flag:
*main.py* — New feature implementation :
```python
# Note that we would usually parse the cli, then pass the flag to the experiment function.
def experiment(new_feature: bool = False):
    # Let's imagine our new feature is model-specific.
    # We start by loading the data.
    data = load_data()
    # Then, we create the model.
    if new_feature:
        model = ModelWithNewFeature()
    else:
        model = Model()
    # Finally, we train and evaluate the model.
    return train_and_evaluate(model, data)
```
Run it with:
```bash
python main.py --new_feature
# We can also run the original experiment without the new feature.
python main.py
```

By following this coding habit, you can easily reproduce previously run experiments by simply passing the same 
configuration. Note that most deep learning algorithms are nondeterministic by nature, which can lead to variations in 
the final performance. However, by using this methodology, you can ensure that it is, in fact, the same code that is 
being run, and that any differences with the previous run is due to the inherent randomness, not due to code changes. 
If you prefer even more reproducibility, nothing stops you from setting seeds and make the algorithms more 
deterministic.

## Configuration management
Since the configuration of each experiment is a crucial aspect in the deepboard way, we determined two main types of 
configurations: configuration file and command line arguments. We recommend to put most parameters in the configuration 
file, and use command line arguments only for parameters that are likely to change often. 

> For new features, we recommend adding a new parameter in the configuration file, and add a default value for it when 
> it is not present.

## Mistakes can happen
Despite our best efforts, mistakes can still happen, and we might change the code without making it optional through a 
parameter. This will render prior experiments unreproducible since not the same code will be run with the same 
configuration. To mitigate this risk, deepboard automatically saves the git commit hash and the diff at each experiment 
run. This makes it easier to revert back to a previous version of the code if needed. 

> While it is possible to revert back to a previous commit, we recommend not to rely on this feature, and consider it as a 
> safety net.