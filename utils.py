def read_data(columns,filename="train_data.txt"):
  columns=columns
  res=[]
  with open(filename)as f:
    for line in f:
      new=[]
      values=line.split(',')
      d={}
      for i,j in zip(values,columns):
        if j=='class' or j=='ID':


          d[j]= int(i)
        else:
          d[j]=i
      res.append(d)
    
    return res


def read_test(columns,filename="test_data.txt"):
  columns=columns
  res=[]
  with open(filename)as f:
    for line in f:
      new=[]
      values=line.split(',')
      d={}
      for i,j in zip(values,columns):
        if j=='class' or j=='ID':


          d[j]= int(i)
        else:
          d[j]=i
      res.append(d)
    
    return res




