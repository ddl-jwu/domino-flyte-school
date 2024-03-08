from utils.job import define_job
from flytekit import workflow, task
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

# pyflyte run --remote types-workflow.py types_workflow
@workflow
def python_workflow(string_input: str = "Hello", int_input: int = 5): 

    job = define_job(name="Dummy job", command="sleep 25")
    job()

    return 
