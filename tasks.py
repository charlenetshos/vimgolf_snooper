from invoke import task, run, Collection

@task
def install_dependencies():
    run(". .vimgolf_ve/bin/activate && pip install -r requirements.txt")

@task
def unit():
    print "Running unit tests..."
    run("python -m unittest discover -s tests/unit -p 'test_*.py'")

@task
def integration():
    print "Running integration tests..."
    run("python -m unittest discover -s tests/integration -p 'test_*.py'")

@task
def all():
    print "Running all tests..."
    run("python -m unittest discover -s tests -p 'test_*.py'")

@task
def start():
    run(". .vimgolf_ve/bin/activate && python snooper.py")
    

tests = Collection(unit, integration, all)

ns = Collection()
ns.add_collection(tests, 'test')

other_tasks = ['install_dependencies', 'start']

for task in other_tasks:
    ns.add_task(eval(task))
