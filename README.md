# JDL: Jupyter Dali Launcher
A simple wrapper of `jupyter` to start jupyter lab in dali

# usage
To activate this wrapping you first need to make `jdl_config.sh`.
Refer to `jdl_config.sh.sample`.

And then, add the following line in your `.bash_profile`
```
export PATH=/path/to/jdl/bin:$PATH
```
Then you can start jupyter lab in dali via ssh connection with the command
```
$ jupyter dali
```
