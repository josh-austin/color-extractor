import sys, os

class Extractor:
    def __init__(self, prefix=''):
        self.variables = {}
        self.prefix = os.path.basename(prefix)
        
    '''
    Returns the variable name if a variable with
    the value <target> is found.
    '''
    def find_variable_name(self, value):
        for var, val in self.variables.items():
            if value == val:
                return var
    
    '''
    Scans a list of <lines> containing CSS and
    returns a list of strings containing the
    rendered LESS version.
    '''
    def scan(self, lines):
        yield "@import '%s_variables.less'\n\n" %self.prefix
        for line in lines:
            found_prop = False
            for prop in ('background-color', 'background', 'color'):
                if prop in line:
                    found_prop = True
                    value = line.split(':')[1].strip().replace('}', '')
                    if not (value in self.variables.values()):
                        self.variables['@var%i' %(len(self.variables) + 1)] = value
                    yield line.replace(value, self.find_variable_name(value) + ';')
            if not found_prop:
                yield line

    '''
    Returns the output for the variables.less
    file as a list of strings
    '''
    def get_variables(self):
        for var, val in self.variables.items():
            yield var + ': ' + val 
            

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            name = '.'.join(path.split('.')[:-1])
            extractor = Extractor(name)
            read = open(path)
            write = open(name + '.less', 'w')
            variables = open(name + '_variables.less', 'w')
            try:
                for line in extractor.scan(read.readlines()):
                    write.write(line)
                for line in extractor.get_variables():
                    variables.write(line + os.linesep)
            finally:
                variables.close()
                write.close()
                read.close()    
            
    else:
        print('usage: python extract.py [file]')
        

