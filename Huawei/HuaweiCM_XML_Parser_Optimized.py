# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 10:17:21 2016

@author: Gerardo Alfredo Alarcon Rivas
"""
import sys
import timeit

def remove_duplicates(li):
    my_set = set()
    res = []
    for e in li:
        if e not in my_set:
            res.append(e)
            my_set.add(e)
    #
    return res

def clean(filename_):
    filedata = None
    with open(filename_, 'r') as file :
        filedata = file.read()

# Replace the target string
    filedata = filedata.replace('\a', '|')

# Write the file out again
    with open(filename_, 'w') as file:
        file.write(filedata)
"""This function create a new file(file_) or open this if is existent and and a new line at the end
    -Use file_ as filename input(this one use directory and filename).
    -Use cadena as a input to write this at the end of the file """
def logger(cadena,file_):
         f = open(file_,'a')
         f.write(cadena+"\n") # python will convert \n to os.linesep
         f.close()

'''
This is the main function, this is doing all the parse tasks.
    -XML_FILE is the name of the xml file to be parsed including the directory.
    -OutPut_dir is the name of thedirectory where the parsed file will save the tables.
'''

def HWCMParser(XML_FILE,OutPut_dir):#
    headers=[]    
    lines=[]  
    temp={}
    MO=[]
    file_output={}
    start_time = timeit.default_timer()
    print "Start Time:",start_time
    Date_file=str(list(filename.split("_"))[-1]).replace(".xml","")
    clean(XML_FILE)# clean the file of one wrong character in the xml file
    
    import xml.etree.ElementTree as ET
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    for node in root.findall('MO'):
       # print node.text
        for child1 in node.findall('attr'):
            temp.update({dict(child1.attrib).get('name'):str(child1.text)})
            RNC_name=temp.get('name')
        for key in temp:
            headers.append(str(key))
            lines.append(str(temp.get(key)))
        headers.insert(1,"Date")
        lines.insert(1,Date_file)
        #logger('*'+dict(node.attrib).get('className')+ '*',OutPut_dir)
        logger('\t'.join(headers),OutPut_dir+RNC_name+'_'+str(dict(node.attrib).get('className'))+'.txt')
        logger('\t'.join(lines),OutPut_dir+RNC_name+'_'+str(dict(node.attrib).get('className'))+'.txt')
        for child1 in node.findall('MO'):
            MO.append(dict(child1.attrib).get('className'))
        MO = sorted(set(MO))
        for key in MO:
            file_output.update({key:None})
        #print file_output
        
        for child1 in node.findall('MO'):
           # print (str(dict(child1.attrib).get('className')))
            if file_output.get(str(dict(child1.attrib).get('className')))==None:
                headers=[]                
                for child2 in child1:
                    #print dict(child2.attrib).get('name')
                    
                    headers.append( dict(child2.attrib).get('name'))
                    
                #print headers
                file_output.update({str(dict(child1.attrib).get('className')):'\t'.join(headers)}) 
        #print file_output
        for n in MO:
            #logger ('*'+n+'*',OutPut_dir+"_"+n+'.txt')
            logger (Date_file+"\t"+file_output.get(n),OutPut_dir+RNC_name+'_'+n+'.txt')
            for child1 in node.findall('MO'):
               if dict(child1.attrib).get('className')==n:
                   lines=[]                
                   for child2 in child1:
                        lines.append(str(child2.text))
                   
                   logger ('\t'.join(lines),OutPut_dir+RNC_name+'_'+n+'.txt')
        
        
         
        
         
            #for key in temp:
             #   print temp.get('name'),child1.text            
   
   
HWCMParser('C:/Users/VervebaMX2/Documents/Projects/XML_Parsing/TEst/huawei/Lte/CMExport_LCUA8008_10.251.40.167_2016091305.xml','C:/Users/VervebaMX2/Documents/Projects/XML_Parsing/TEst/huawei/Lte/')

#first_arg = sys.argv[1]
#second_arg = sys.argv[2]

#if __name__ == "__main__":
#     HWCMParser(first_arg,second_arg)   
   
   
   
   