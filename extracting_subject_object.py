#It includes :
#1.removing predicate
#2.removing "." from language tag
#3.concatenating subject,object and language tags, separated by "\t".

import pip
import pandas as pd

df=pd.read_csv("short_abstracts_copy_tab.csv", sep='\t' ,header=None) #,engine="python", quoting=None) #,delimiter=" "skiprows=5,
print(df.shape)


#separating subject from predicate
df.columns=["subject_predicate","object","lang_tag"]
df_subject=df["subject_predicate"]
df_subject.to_csv("subject_predicate.csv",index=False,header=None)

#writing object to object.csv
df_object=df["object"]
df_object.to_csv("object.csv",index=False,header=None)


#writing languagetag+"." to lang_tag.csv
df_lang_tag=df["lang_tag"]
df_lang_tag.to_csv("lang_tag.csv",index=False,header=None)


#separating subject and predicate and removing predicate
df_sp=pd.read_csv("subject_predicate.csv", sep=' ',header=None)
df_sp=df_sp[0]
df_sp.to_csv("subjetonly.csv",header=None,index=False)
#print(df3[[0]])

#removing "." from language tag
df_l=pd.read_csv("lang_tag.csv",sep=' ',header=None)

#concatenating (subject) , (object with language tag)
df_concat_ol=pd.concat([df_object,df_l[0]],axis=1)

df_concat_ol.to_csv("concat_1.csv",sep=' ',index=False,header=None)
concat_1=pd.read_csv("concat_1.csv",sep='\t',header=None)
df_sp=pd.read_csv("subjetonly.csv", sep=' ',header=None)
df_concat_s_ol=pd.concat([df_sp[0],concat_1],axis=1)
df_concat_s_ol.to_csv("concatenated_sa.csv",index=False,header=None,sep='\t')

