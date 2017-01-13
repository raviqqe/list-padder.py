VENV_DIR = '.venv'


def vsh *args
  sh ". #{VENV_DIR}/bin/activate && #{args.join ' '}"
end


task :test do
  sh "python3 -m venv #{VENV_DIR}"
  vsh 'pip install pytest'
  vsh 'pytest --doctest-modules listpad'
end


task :upload => :test do
    sh 'python3 setup.py sdist bdist_wheel'
    sh 'twine upload dist/*'
end


task :clean do
  sh 'git clean -dfx'
end
