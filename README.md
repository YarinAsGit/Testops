# Testops

Testops is a python library that let you write scripts to preform integration tests on machines without knowing pythons using write a uniqe script file.
You can starts the tests from anypoints, for example, if your are working with dockers you can start the tests at the end of an entry.sh shell script, of course the best practice is to run the script when your machine finished loading and configured the necessary resources.

## TestopsFile
A script file anyone can learn and write himself, picking exactly what tests to run on the machine, and files/directories exists, open ports, running webservers, access to other hosts.

### Example of TestopsFile
```
INSTALLED_PLUGINS plugins=["base"]

# Env vars checks
RUN_CHECK env-var var_name="SHLVL" var_value="1"
RUN_CHECK env-var var_name="XPC_SERVICE_NAME"

# Ports check
RUN_CHECK local-open-ports ports=[8888,7777]

# Check logs dirs
RUN_CHECK dirs-exists dirs=["/tmp/logs/web", "/tmp/logs/nginx"]

# Check pulled git repos
RUN_CHECK dirs-exists dirs=["/opt/workdir/ui-repo", "/opt/workdir/be-repo"]

# Check config created
RUN_CHECK files-exists files=["/opt/workdir/config.json"]
```

### Creating commands and sub-commands yourself
You can use python and creates your own command and sub-commands and preform a custom checks that fir your creteria.

## Plugins
Plugins are groups of checks you can preform. The base plugin contains a lot of useful and common checks you can read about in the documentation.
There is a lot of other plugins you can import and use, for example aws_plugin contains a lot of checks you can preform from your machine related to aws services, for example, check accessing to s3 buckets.
