from time import sleep
# declare all registers and memory
ram=[["LOAD",5],["ADD",6],["STO",7],None,None,12,8,None]
pc=0
mar=0
acc=[]
mdr=[]
cir=[]

#defining the functions of the CPU
def load():
  global mdr, acc
  value=ram[mdr[1]]
  acc.append(value)

def add():
   global acc, mar
   value=ram[mdr[1]]
   acc.append(value)
   acc=[sum(acc)]
   return acc

def store():
   global acc, mar, mdr, cir
   ram[mdr[1]]=acc

def get_from_ram():
    return ram[mar]
  
def fetch():
  global pc, mar, mdr, cir
  mar=pc
  pc+=1
  mdr=get_from_ram()
  
def decode():
  global mdr, cir
  cir=mdr

def excecute():
  global cir
  if cir[0]=="LOAD":
    load()
  elif cir[0]=="ADD":
    add()
  elif cir[0]=="STO":
    store()

fde_n=0

while ram[pc]!=None:
  fde_n+=1
  print(fde_n)
  sleep(2)
  print(f"\nPC: {pc}\n ")
  fetch()
  print(f"Fetch\n PC: {pc}\n MAR: {mar}\n MDR: {mdr}\n ACC: {acc}\n ")
  sleep(2)
  decode()
  excecute()
  print(f"Excecute\n PC: {pc}\n MAR: {mar}\n MDR: {mdr}\n ACC: {acc}\n ")
  sleep(2)
