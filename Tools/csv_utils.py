# Constants
MIN_PER_SEC = 1 / 60


def extract_values_by_header(data, main_field: str, sub_field: str = None):
    """Get values for given field

    Args:
        data: DeskCycle data set
        main_field (str): 1st field name
        sub_field (str): 2nd field name (use only for "Seconds" field in time)

    Returns:
        field_values (list): list of values for given field
    """

    field_values = []

    # Skip null/NaN values for now
    if sub_field is None:
        nan_idx = list(data[data[main_field].isnull()].index)
    else:
        nan_idx = set(list(data[data[main_field].isnull()].index) + \
                      list(data[data[sub_field].isnull()].index))

    for i in range(len(data.index)):
        if i in nan_idx:
            field_values.append("")
        else:
            if sub_field is None:
                field_values.append(data.loc[i, main_field])
            else:
                field_values.append(data.loc[i, main_field] + (data.loc[i, sub_field] * MIN_PER_SEC))

    return field_values
