class MonitorConfiguration:
    TAG_OUTPUT="type_output"
    TAG_LANGUAGE="language"
    TAG_COMPANY="company"
    TAG_MODEL="models"
    TAG_CUSTOMLABEL="custom_label"
    TAG_PARAMETERS="parameters"
    TAG_PARAMETER_TAG="tag"
    TAG_PARAMETER_CARD="card"
    TAG_PARAMETER_TYPE="type"
    TAG_PARAMETER_SEARCH="search"
    TAG_PARAMETER_DEEP="deep"
    TAG_PARAMETERS_RELATIVE="parameters_relative"
    TAG_PARAMETERS_RELATIVE_TAG_RELATIVE="tag_relative"
    TAG_PARAMETERS_RELATIVE_NEAR="near_label_or_value"
    TAG_CUSTOM_CONFIGURATION="configuration_id"
    def __init__(self, json_data):
        self.json_data = json_data