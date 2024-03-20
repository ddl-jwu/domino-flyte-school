from utils.flyte import run_domino_job, Input, Output
from flytekit import workflow
from flytekit.types.file import FlyteFile
from flytekit.types.directory import FlyteDirectory

'''
To run this workflowp, execute the following line in the terminal

pyflyte run --remote training-workflow.py training_workflow
'''
@workflow
def training_workflow(data_path: FlyteFile="/mnt/code/data/data.csv") -> FlyteFile: 
    """
    Sample data preparation and training workflow

    This workflow accepts a path to a CSV for some initial input and simulates
    the processing of the data and usage of the processed data in a training job.

    :param data_path: Path of the CSV file data
    :return: The training results as a model
    """

    data_prep_results = run_domino_job(
        name="Prepare data",
        environment="Spark environment",
        hardware_tier="Large-CPU",
        command="python /mnt/code/python/prep-data.py",
        inputs=[
            Input(name="data_path", type=FlyteFile, value=data_path)
        ],
        outputs=[
            Output(name="processed_data", type=FlyteFile)
        ]
    )

    training_results = run_domino_job(
        name="Train model",
        environment="Ray environment",
        hardware_tier="Large-GPU",
        command="python /mnt/code/python/train.py",
        inputs=[
            Input(name="processed_data", type=FlyteFile, value=data_prep_results['processed_data']),
            Input(name="epochs", type=int, value=10),
            Input(name="batch_size", type=int, value=32)
        ],
        outputs=[
            Output(name="model", type=FlyteFile)
        ]
    )

    return training_results['model']
