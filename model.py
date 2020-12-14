from pycaret.utils import version
version()
from pycaret.datasets import get_data
data = get_data('insurance')
from pycaret.regression import *
reg1 = setup(data, target = 'charges', session_id=123, log_experiment=True, experiment_name='insurance1')
from pycaret.regression import *
r2 = setup(data, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True,
           feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'])

best_model = compare_models(fold=5)

lr = create_model('lr')

save_model(lr, model_name = 'deploy_model')


