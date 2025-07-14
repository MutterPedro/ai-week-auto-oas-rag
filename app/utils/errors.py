class SchemaInferenceError(Exception):
    """Error raised when schema inference fails"""
    pass

class AuthPatternDetectionError(Exception):
    """Error raised when authentication pattern detection fails"""
    pass

class EndpointAnalysisError(Exception):
    """Error raised when endpoint analysis fails"""
    pass