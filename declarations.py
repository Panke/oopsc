class Declaration(object):
    """
    Baseclass of all Declarations
    """

    def __init__(self, identifier):
        self.identifier = identifier

class ClassDeclaration(Declaration):
   
    def __init__(self, ident):
        Declaration.__init__(self, ident)
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

    def add_member(self, member):
        """
        Add a member to the class
        """
        if isinstance(member, MethodDeclaration):
            methods.append(member)
        else:
            #member is a list of variable declarations
            self.vars.extend(member)

class MethodDeclaration(Declaration):
    """
    Declaration of a method
    """

    def __init__(self, ident):
        Declaration.__init__(self, ident)
        self.statements = []
        self.vars = []


    def add_statement(self, stmt):
        self.statements.append(stmt)

    def add_var(self, var):
        self.vars.append(var)

class VariableDeclaration(Declaration):
    """
    Declaration of a variable
    """

    def __init__(self, ident, type=None):
        Declaration.__init__(self, ident)
        self.type = type

