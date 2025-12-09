from typing import Dict, Any


class TemplateEngine:
    """
    Very simple template engine:
    - Accepts a dict template
    - Uses {{var_name}} placeholders
    - Replaces placeholders with values from context
    - If the entire string is a single placeholder and the context value
      is a list/dict, it returns that list/dict directly (not as a string)
    """

    def __init__(self, template: Dict[str, Any]):
        self.template = template

    def render(self, context: Dict[str, Any]) -> Dict[str, Any]:
        def replace(value):
            # Case 1: placeholder in a string
            if isinstance(value, str):
                # If string is exactly one placeholder like "{{questions_list}}"
                for key, val in context.items():
                    placeholder = f"{{{{{key}}}}}"
                    if value == placeholder:
                        # Return raw value (dict/list/str/number)
                        return val

                # Otherwise, do normal text replacement
                for key, val in context.items():
                    placeholder = f"{{{{{key}}}}}"
                    value = value.replace(placeholder, str(val))
                return value

            # Case 2: nested dict
            if isinstance(value, dict):
                return {k: replace(v) for k, v in value.items()}

            # Case 3: list
            if isinstance(value, list):
                return [replace(v) for v in value]

            # Other types (int, float, bool, None)
            return value

        return replace(self.template)
