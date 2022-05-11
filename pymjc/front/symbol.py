class Symbol():
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    dictionary = {}

    def to_string(self):
        return self.name

    
    def symbol(name: str):
        symbol: Symbol = Symbol.dictionary[name]
        
        if symbol is None:
            symbol = Symbol(name)
            Symbol.dictionary[name] = symbol

        return symbol

class MethodEntry():

    def __init__(self, type) -> None:
        self.return_type = type
        self.locals = {}
        self.param = {}
        self.param_list = []

    def get_params(self):
        return self.param

    def get_param(self, id: str):
        return self.param[Symbol.symbol(id).to_string()]

    def get_locals(self):
        return self.locals

    def get_locals(self, id: str):
        return self.locals[Symbol.symbol(id).to_string()]        

    def get_num_params(self) -> int:
        return self.param_list.size()

    def get_param(self, pos: int):
        return self.param_list[pos]

    def get_return_type(self): 
        return self.return_type

    def add_local(self, id: str, type) -> bool:
        if(self.contains_local(Symbol.symbol(id)) or self.contains_param(Symbol.symbol(id))):
            return False
        else:
            self.locals[Symbol.symbol(id).to_string()] = type

        return True


    def add_param(self, id: str, type) -> bool:
        if(self.contains_param(Symbol.symbol(id))):
            return False
        else:
            self.param[Symbol.symbol(id).to_string()] = type
            self.param_list.append(type)
        
        return True

    def contains_local(self, id: str) -> bool:
        return Symbol.symbol(id).to_string() in self.locals.keys()

    def contains_param(self, id: str) -> bool:
        return Symbol.symbol(id).to_string() in self.param.keys()




class ClassEntry():

    def __int__(self):
        self.fields = {}
        self.methods = {}
        self.supper_class_id = None

    def __int__(self, supper_class_id: str):
        self.fields = {}
        self.methods = {}
        self.supper_class_id = supper_class_id


    def get_supper_class_id(self):
        return self.supper_class_id

    def get_fields(self):
        return self.fields

    def get_field(self, id: str):
        return self.fields[Symbol.symbol(id).to_string()]
    
    def get_methods(self):
        return self.methods

    def get_method(self, id: str) -> MethodEntry:
        return self.methods[Symbol.symbol(id).to_string()]    
    
    def add_var(self, id : str, type) -> bool:
        if(self.contains_field(Symbol.symbol(id))):
            return False
        else:
            self.fields[Symbol.symbol(id).to_string()] = type
        
        return True

    def add_method(self, id: str, entry: MethodEntry) -> bool:
        if(self.contains_method()):
            return False
        else:
            self.methods[Symbol.symbol(id).to_string()]= entry
    
        return True

    def contains_field(self, id: str) -> bool:
        return Symbol.symbol(id).to_string() in self.fields.keys()
    

    def contains_method(self, id: str) -> bool:
        return Symbol.symbol(id).to_string() in self.methods.keys()



class SymbolTable():
    

    def __init__(self) -> None:
        self.class_scopes = {}
        self.curr_class = None
        self.curr_method = None
        self.curr_class_name = None
        self.curr_method_name = None        
        pass

    def contains_key(self, id: str) -> bool:
        return Symbol.symbol(id).to_string() in self.class_scopes

    def get_class_entry(self, id: str) -> ClassEntry:
        return self.class_scopes[Symbol.symbol(id).to_string()]

    def set_curr_class(self, id: str) -> None:
        self.curr_class = self.class_scopes[Symbol.symbol(id).to_string()];      
        self.curr_class_name = id
        self.curr_method = None
        self.curr_method_name = None

    def set_curr_method(self, id: str):
        self.curr_method = self.curr_class.get_methods()[Symbol.symbol(id).to_string()]
        self.curr_method_name = id

    def add_scope(self, id: str, entry: ClassEntry) -> bool:
        self.curr_class = entry
        self.curr_class_name = id
        self.curr_method = None
        self.currMethodName = None
        if(self.contains_key(Symbol.symbol(id).to_string())):
            return False
        else:
            self.class_scopes[Symbol.symbol(id).to_string()] = entry
        
        return True

    def add_extends_entry(self, id: str, supper_class_id: str) -> None:

        base: ClassEntry = self.get_class_entry(Symbol.symbol(id).to_string())
        supper_class: ClassEntry = self.get_class_entry(Symbol.symbol(supper_class_id).to_string())

        for supper_field_id in supper_class.get_fields().keys():
            base.add_var(supper_field_id, supper_class.get_field(supper_field_id))
        
        for supper_method_id in supper_class.get_methods().keys():
            base.add_method(supper_method_id, supper_class.get_method(supper_method_id))


    def add_method(self, id: str, entry: MethodEntry) -> bool:
        self.curr_method = entry
        self.curr_method_name = id
        if(self.curr_class.add_method(id, entry)):
            return True
        else:
            return False
        

    def add_field(self, id: str, type) -> bool:
        return self.curr_class.add_var(id, type)

    def add_param(self, id: str, type) -> bool:
        return self.curr_method.add_param(id, type)

    def add_local(self, id: str, type) -> bool:
        return self.curr_method.add_local(id, type)