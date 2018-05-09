# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 14:26:05 2018
处理para_inputs.txt的数据,看每个参数的变化.
@author: niu
version: 01
"""

'''
把所有数据放到一个文件中
version: 02
'''
import os

d='D:/DMFTdata/two_nnn/find_parameters/20180508/k=1.0/'
for k in range(1,11):
    m=k/10
    infile=d+'t2_t1={}'.format(m)   
    os.chdir(infile)
    dirs=os.getcwd()
#处理t2_t1=m下的文件夹    
    for i in range(1,51):
        j='{:.2f}'.format(i/100)
#        dirs='C:/Users/niu/Desktop/50/'
        inf='/'+j+'/para_inputs.txt'
        outf='/'+j+'/parameters.txt'
        input_dir=dirs+inf
        output_dir=dirs+outf
        with open(output_dir,'wt') as p,open(input_dir,'rt') as ps:
            for index,line in enumerate(ps):
                if index % 10==0 and index!=0:
                    line=line
                    p.write("\n")
                else:
                    line=line.strip('\n')#去掉每行的换行符
                    if (index-2) % 10==0:
                        p.write(line)
                    elif (index-3) % 10==0:
                        p.write(line)
                    elif (index-4) %10==0:
                        p.write(line)
                    elif (index-7) % 10==0:
                        p.write(line)
                    elif (index-8) % 10==0:
                        p.write(line)
                    elif (index-9) % 10==0:
                        p.write(line)
