class Argument:
    def __init__(self, args):
        self.args = args
        self.commands = []
        self.options = []
        self.optionValues = {}

        for arg in args:
            if "-" in arg:
                if "=" in arg:
                    pair = arg.split("=")
                    self.optionValues[pair[0]] = pair[1]
                    self.options.append(pair[0])
                else:
                    self.options.append(arg)
            else:
                self.commands.append(arg)

    def hasOptions(self, options: list):
        useroptions = set(self.options)
        reqoptions = set(options)
        return len(list(useroptions & reqoptions)) == len(options)
    
    def hasOption(self, option):
        return self.hasOptions([option])
    
    def hasOptionValue(self, option):
        return option in self.optionValues
    
    def hasCommands(self, commands):
        usercommands = set(self.commands)
        reqcommands = set(commands)
        return len(list(usercommands & reqcommands)) == len(commands)
    
    def hasCommand(self, command):
        return self.hasCommands([command])
    
    def getOptionValue(self, option):
        if option in self.optionValues:
            return self.optionValues[option]
        else:
            return None