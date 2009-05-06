# coding: utf-8 

def indentby(length, string):
        from StringIO import StringIO as sio
        return '\n'.join(map(lambda x: length * '\t' + x, string.split('\n')))+'\n'



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
            self.methods.append(member)
        else:
            #member is a list of variable declarations
            self.vars.extend(member)


    def __str__(self):
        s = 'CLASS %s\n:' % self.identifier
        if self.vars:
            s += indentby(1, "VARIABLES:\n")
            for var in self.vars:
                s += indentby(2, str(var) + '\n')
        if self.methods:
            s += indentby(2, "\t" + "METHODS:\n")
            for met in self.methods:
                s += indentby(2, str(met) + '\n')

        return s

    
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

    def __str__(self):
        s = 'METHOD %s' % self.identifier +'\n'
        if self.vars:
            s += indentby(1, 'VARS:\n')
            for v in self.vars:
                s += indentby(2, str(v) + '\n')
        if self.statements:
            s +=  indentby(1, 'STATEMENTS:\n')
            for stat in self.statements:
                s += indentby(2, str(stat))

        return s
    
class VariableDeclaration(Declaration):
    """
    Declaration of a variable
    """

    def __init__(self, ident, type=None):
        Declaration.__init__(self, ident)
        self.type = type

    def __str__(self):
        return 'VarDecl: %s : %s' % (self.identifier, str(self.type))
        
    def __repr__(self):
        return str(self)
    
intType = ClassDeclaration('intType')
boolType = ClassDeclaration('boolType')
nullType = ClassDeclaration('nullType')
