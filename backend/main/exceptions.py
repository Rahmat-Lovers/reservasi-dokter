from ninja.errors import ValidationError
import json as _json

class ValidationError(ValidationError):
    def __init__(self, form):
        super().__init__(
            _json.loads(form.errors.as_json())
        )