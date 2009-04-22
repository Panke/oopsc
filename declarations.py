class Declaration(object):
    """
    Baseclass of all Declarations
    """

    def __init__(self, identifier):
        self.identifier = identifier

class ClassDeclaration(Declaration):
   
    def __init__(self):
        # size of the class header used for organisation of each object
        headersize = 0

        # size of the object, will be calculated later
        # TODO: does it include the headersize? 
        self.objectsize = 0
        # variables of this class
        self.vars = []
        # methods of this class
        self.methods = []
        # declarations visible in this class
        self.declarations = []
