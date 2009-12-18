#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Description', 're_depends', 're_atom', 're_pkg_atom']

import re, os

# octave-forge DESCRIPTION's dependencies atoms
re_depends = re.compile(r'([a-zA-Z]+) *(\(([><=]?=?) *([0-9.]+)\))?')

# gentoo-like atoms, to use with emerge/whatever package manager
re_atom = re.compile(r'^([><]?=?)([a-zA-Z\-/]+)(-(.*))?$')

# we'll use atoms like 'control' or 'control-1.0.11' to g-octave packages
re_pkg_atom = re.compile(r'^(.+)-([0-9.]+)$')


class DescriptionException(Exception):
    pass


class Description(object):
    
    def __init__(self, file):
        
        if not os.path.exists(file):
            raise DescriptionException('File not found: %s' % file)
        
        fp = open(file)
        myfile = fp.readlines()
        fp.close()
        
        kw = ''
        
        self.__desc = {}
        
        for i in myfile:
            line = i.split(':')
            if len(line) != 2:
                if i[0].isspace() and kw != '':
                    self.__desc[kw] += ' ' + i.strip()
            else:
                kw = line[0].strip().lower()
                if self.__desc.has_key(kw):
                    if kw == 'depends' or kw == 'systemrequirements' or kw == 'buildrequires':
                        self.__desc[kw] += ', ' + line[1].strip()
                    else:
                        self.__desc[kw] += ' ' + line[1].strip()
                else:
                    self.__desc[kw] = line[1].strip()
                 
        for i in self.__desc:
            if i == 'depends':
                self.__desc[i] = self.__depends(self.__desc[i])
            if i == 'systemrequirements' or i == 'buildrequires':
                self.__desc[i] = self.__requirements(self.__desc[i])
    
    
    def __depends(self, long_atom):
        
        tmp = []
        
        for atom in long_atom.split(','):
            
            r = re_depends.match(atom.strip())
            
            if r != None:
                
                myatom = ''
                
                if r.group(3) != None:
                    myatom += str(r.group(3)) == '==' and '=' or str(r.group(3))
                
                if r.group(1) == 'octave':
                    myatom += 'sci-mathematics/octave'
                else:
                    myatom += 'g-portage/%s' % r.group(1)
                
                if r.group(4) != None:
                    myatom += '-%s' % r.group(4)
                
                tmp.append(myatom)
        
        return tmp
    
    
    def __requirements(self, long_atom):
        
        tmp = []
        
        for atom in long_atom.split(','):
            tmp.append(atom.strip())
        
        return tmp

    
    def __getattr__(self, name):
        
        if self.__desc.has_key(name):
            return self.__desc[name]
        
        return None


if __name__ == '__main__':
    a = Description('/development/contrib/octave-forge-20090607/main/image-1.0.10/DESCRIPTION')
    print a.depends