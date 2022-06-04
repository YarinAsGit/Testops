

class CheckParam:

    def __init__(self, param_type, required: bool = False):
        self.param_type = param_type
        self.required = required

    def parse(self, raw_val: str):
        """
        Cast the raw value by type, raise exception if failed.
        """
        return self.param_type(raw_val)


class BaseCheck:
    """
    BaseCheck class represent a check you can preform.
    Should include preform_check func and to contain all the check params of the Check
    """

    def __init__(self, **kwargs):
        params = self.get_params()
        required_params_name = self.get_params_list()['required']
        input_params = set(kwargs.keys())

        # Check all required params received
        required_check_result = required_params_name - input_params
        assert not required_check_result, f"Missing required params {required_check_result}"

        for k, v in kwargs.items():
            if k not in params:
                raise Exception(f"Unknown param {k}")

            assert isinstance(params[k], CheckParam), f"{params[k]} is not CheckParam type"
            # Check param's value is valid and return the sanitized value, raise exception otherwise
            parsed_value = params[k].parse()
            setattr(self, k, parsed_value)

    @classmethod
    def get_params(cls) -> dict:
        """
        Returns all the params of the check using dict.
        The key is the param name and the value is an instance of CheckParam.
        """
        return {k: v for k, v in vars(cls).items() if isinstance(v, CheckParam)}

    @classmethod
    def get_params_list(cls) -> dict:
        """
        Returns dict that contains two list, one list contains all the required params and optional params list.
        """
        params = {'required': [], 'optional': []}
        for k, v in cls.get_params():
            if v.required:
                params['required'].append(k)
            else:
                params['optional'].append(k)
        return params

    def preform_check(self) -> None:
        raise NotImplementedError

