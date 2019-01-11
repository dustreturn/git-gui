#coding=utf-8


#追踪untracked files

import os

import subprocess



from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import numpy as np
import pandas as pd
import threading

from tkinter import filedialog

class untrack(Frame):
    
  
  def __init__(self,master=None):
      Frame.__init__(self,master)
      self.grid()
      self.content()
      

  def content(self):

#insert Entry
      def choosefile(a):
        if self.valueputin.get() !="":
          self.valueInput=self.valueputin.get()
        else:
          self.valueInput=filedialog.askdirectory()
        print (self.valueInput)



      self.lf = ttk.LabelFrame(self, text="文件搜索")
      # self.lf.pack(fill=X, padx=15, pady=8,side=RIGHT)
      # self.lf.grid(row=0,column=0,padx=10,pady=10)






      def clear_all(a):
          self.T.config(state=NORMAL)
          self.T.delete(1.0,END)
          self.e1.delete(1.0,END)
          x=self.tree.get_children()
          for item in x:
              self.tree.delete(item)
          y=self.tree2.get_children()
          for item in y:
              self.tree2.delete(item)
          z=self.tree4.get_children()
          for item in z:
              self.tree4.delete(item)

          q=self.tree3.get_children()
          for item in q:
              self.tree3.delete(item)

          w=self.tree3_2.get_children()
          for item in w:
              self.tree3_2.delete(item)
          v=self.tree6.get_children()
          for item in v:
              self.tree6.delete(item)
         
                            
                                          
                                                                      
      def clear_all2(a):

          q=self.tree5.get_children()
          for item in q:
              self.tree5.delete(item)

      def clear_all3(a):

          q=self.tree5_2.get_children()
          for item in q:
              self.tree5_2.delete(item)
              
      def clear_all4(a):
          q=self.tree6.get_children()
          for item in q:
              self.tree6.delete(item)

      #add function
      def addto(a):
#          print(self.valueInput.get())
          keyvalue=self.valueInput
          t=self.tree2.get_children()
          for i in t:
              
              zz=self.tree2.item(i,'values')
              print(zz)
              z=zz[0]
              print(z)

              cmd1=r'git add '
              cmd2=cmd1 + z
  
              cmd=cmd2
              print(keyvalue)
              cmdpath=str(keyvalue)
  
              process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
  
              stdout=process.communicate()
  
              process.wait()
              result=process.returncode
          y=self.tree2.get_children()
          for item in y:
              self.tree2.delete(item)
              
      #commit function
      
      def commit1():
          y=self.tree4.get_children()
          for item in y:
              self.tree4.delete(item)

#          print(self.valueInput.get())
          keyvalue=self.valueInput
          cmd=r'git log'
          cmdpath=str(keyvalue)
  
          process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
  
          stdout=process.communicate()
  
          print("stdout",stdout)
          process.wait()
          result=process.returncode
          stdout=str(stdout)
          stdout=stdout[3:-1]
          L=stdout.split('\\n')
          L=np.array(L)
          print(L)
          L1=L.reshape(-1,6)#-1表示不知道有多少行，或者说最后一行
          L2=pd.DataFrame(L1)
          L2[0]=L2[0].str.slice(6,-1)
          L2[1]=L2[1].str.slice(7,-1)
          L2[2]=L2[2].str.slice(5,-1)

          print(L2)
          for indexs in L2.index:
             self.tree4.insert("","end",values=(L2.loc[indexs][0],L2.loc[indexs][1],L2.loc[indexs][2],L2.loc[indexs][4]))
             print(indexs)
             
      def commit_v():
          version = askstring('Name','Reason for commit?')
          version='"'+str(version)+'"'
          keyvalue=self.valueInput
          cmd=r'git commit -m '
          cmd=cmd+version
          cmdpath=str(keyvalue)
  
          process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
   
 
 
          
#show the branches         
      def branch():

          keyvalue=self.valueInput
          cmd=r'git branch '
          cmdpath=str(keyvalue)
  
          process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
   
          stdout=process.communicate()     
          
          # vv=stdout[0]
          # aa=str(vv,'utf-8')
          stdout=str(stdout)
          stdout=stdout[3:-8]
          print(stdout)

          L=stdout.split('\\n')
          
          L=np.array(L)
          L.reshape(1,-1)
          L2=pd.DataFrame(L)

          print(L2)
          for indexs in L2.index:
             cc=L2.loc[indexs][0]
 #            cc=cc.replace(" ","_")
             print(cc)
             self.tree5.insert("",indexs,text=(cc),values=(cc,""))
             # print(self.tree5.get_children(item,"values"))
 
             
 #revision history

      def revision():
          keyvalue=self.valueInput
          y=self.tree6.get_children()
          for item in y:
              self.tree6.delete(item)
              
          cmd=r'git reflog '
          cmdpath=str(keyvalue)
  
          process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
   
          stdout=process.communicate()     
          stdout=str(stdout)
          stdout=stdout[3:-8]
          print(stdout)
          L=stdout.split('\\n')
          L=np.array(L)
          print(L)
          L.reshape(1,-1)
          L2=pd.DataFrame(L)

          L3=L2[0].str.split(r'HEAD@',expand=True)
          # print(L3[4])

          print(L3)
          for indexs in L3.index:

             self.tree6.insert("","end",values=(L3.loc[indexs][0],L3.loc[indexs][1]))




           
 #切换分支
      def selectItem3(a):
           
        curItem=self.tree5.focus()
        zz1=self.tree5.item(curItem)["values"]
 
        print(zz1[0])
           
        keyvalue=self.valueInput
        cmd=r'git checkout '
        cmd=cmd+zz1[0]
        cmdpath=str(keyvalue)
  
        process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
    
        stdout=process.communicate()     

#回到过去版本


      def restoreversion(a):
        curItem=self.tree6.focus()
        zz1=self.tree6.item(curItem)["values"]
        print(zz1[0])
        msg=messagebox.askquestion(title="Restore",message="Restore the file?")
        if msg=='yes':
            keyvalue=self.valueInput
            cmd=r'git reset '+zz1[0]
            cmdpath=str(keyvalue)
            process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
            stdout=process.communicate()   
            
      def restore_temp():
                  # curItem=self.tree3_2.focus()
                  # zz=self.tree3_2.item(curItem)["values"]
           msg=messagebox.askquestion(title="Restore",message="Restore the file?")
           if msg=='yes':

                  print(z)
#                   z=zz[0]
                  keyvalue=self.valueInput
                  cmdpath=str(keyvalue)
                  cmd=r'git checkout '+z
                  process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
                  stdout=process.communicate()
                  process.wait()
                  result=process.returncode
                  print(cmd)

                  
      def add_temp():
           msg=messagebox.askquestion(title="Restore",message="Add to commit?")
           if msg=='yes':

                  keyvalue=self.valueInput
                  cmdpath=str(keyvalue)               
                  cmd=r'git add '+z
                  process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
                  stdout=process.communicate()
                  process.wait()
                  result=process.returncode
                  print(cmd)  
                  
      #initialize the committed file
      
      def initial():
          #判断是否已经备份
          def isGitDir(dir):
             repdir=os.path.join(os.path.abspath('.'),dir)
             repgitdir=os.path.join(repdir,'.git')
             if not os.path.exists(repgitdir):
                     return False
             return True
          file1=filedialog.askdirectory()
          a=np.array([])
          print(file1)
          for parent,dirnames,filenames in os.walk(file1):
               for dirname in dirnames:
                    #print(parent)
                 zz=str(parent)
                 print(zz)
 
                 if zz.find('.git')==-1 & dirname.find('.git')==-1:#用index只会返回value error
                    aaa=os.path.join(parent,dirname)
                    print(aaa)
                    aa=np.array([aaa])
                    print(aa)
                    a=np.concatenate([a,aa])
        
                    print(a)



          for i in a:
    
            file1=str(i)
            #   print(file1)
            if isGitDir(file1)==False:
               cmd1=r'git init'
               cmd=cmd1
               cmdpath=str(i)
               process=subprocess.Popen(cmd,shell=True,cwd=cmdpath)
               process.wait()
               result=process.returncode    
                       

          
#initialize all the files in the location 


      self.menubar = Menu(root)
      self.menubar.add_command(label="Initialize",command=initial)

      self.filemenu=Menu(self.menubar,tearoff=0)
      self.filemenu.add_command(label="Commit Current Version",command=commit_v)
      self.filemenu.add_separator()
      self.filemenu.add_command(label="Commit History",command=commit1)   
      self.filemenu.add_command(label="Revision",command=revision)
      self.filemenu.add_command(label="Branch",command=branch)
      self.filemenu2=Menu(self.menubar,tearoff=0)
      self.filemenu2.add_command(label="Restore",command=restore_temp)   
      self.filemenu2.add_command(label="Add",command=add_temp)
      self.menubar.add_cascade(label="Commit",menu=self.filemenu)
      self.menubar.add_cascade(label="Modified",menu=self.filemenu2)
      
      
      self.menubar.add_command(label="quit",command=root.quit)
      root.config(menu=self.menubar)

      # self.buttoninit=Button(root,text="Initialize")
      # # self.buttoninit.pack(padx=15,fill=X,side=LEFT)   
      # self.buttoninit.grid(row=0,column=0,ipadx=10,ipady=10,)


              
      self.button1=Button(root,text="搜索",command=self.print11)
      # self.button1.pack(padx=15,fill=X,side=LEFT)
      self.button1.grid(row=0,column=0,padx=10,pady=5)   
      self.button1.bind("<Button-1>",clear_all)      

      self.valueputin=Entry(root)
      # self.valueputin.pack(padx=15,fill=X,side=LEFT)
      self.valueputin.grid(row=0,column=1,ipadx=5,columnspan=2)      


    
      # #record the untracked files
      self.tree=ttk.Treeview(root,show="headings",columns=(1),height=6)
      # self.tree.pack(ipadx=30,side=LEFT)
      self.tree.grid(row=1,column=0,ipadx=30,ipady=30)
      self.tree.column(1,width=30)
      self.tree.heading(1,text='Untracked')

      self.tree2=ttk.Treeview(root,show="headings",columns=(1),height=6)
      # self.tree2.pack(ipadx=30,side=LEFT)
      self.tree2.grid(row=1,column=1,ipadx=30,ipady=30)
      self.tree2.column(1,width=30)

      self.tree2.heading(1,text='To Add')
      
      #add file
      self.button2=Button(root,text="add")
      # self.button2.pack(ipadx=15,side=LEFT)
      self.button2.grid(ipadx=15,row=1,column=3,sticky=E)
      self.button2.bind("<ButtonRelease-1>",addto)
      
      #record the deleted files before commited
      
      self.tree3=ttk.Treeview(root,show="headings",columns=(1),height=15)
      self.tree3.column(1,width=30)
      self.tree3.heading(1,text='Deleted')
      # self.tree3.pack(ipadx=30,side=LEFT)   
      self.tree3.grid(row=2,column=1,ipadx=30,ipady=40) 
      #record the modified files before commited
      
      self.tree3_2=ttk.Treeview(root,show="headings",columns=(1),height=15)
      self.tree3_2.column(1,width=30)
      self.tree3_2.heading(1,text="Modified")
      # self.tree3_2.pack(ipadx=30,side=LEFT)
      self.tree3_2.grid(row=2,column=0,ipady=40,ipadx=30)
      
      self.T=Text(root)
      # self.T.pack(ipadx=60,ipady=50,side=LEFT)
      self.T.grid(row=1,column=4,columnspan=3)  
      
      # the log of version
      self.tree4=ttk.Treeview(root,show="headings",columns=(0,1,2,4),height=15)

      self.tree4.column(0,width=50)
      self.tree4.column(1,width=50)
      self.tree4.column(2,width=50)
      self.tree4.column(4,width=50)

      self.tree4.heading(0,text='Number')
      self.tree4.heading(1,text='Committer')
      self.tree4.heading(2,text='Date')
      self.tree4.heading(4,text='Version')
      # self.tree4.pack(side=LEFT,ipadx=160)
      self.tree4.grid(row=2,column=4,columnspan=16,ipadx=180,ipady=40)    
      
        
#       #show the current branch
#       
      self.tree5=ttk.Treeview(root,show="headings",columns=(0,1),height=15)
      self.tree5.column(0,width=100)
      self.tree5.heading(0,text='Branch')
      self.tree5.column(1,width=0)
      self.tree5.heading(1,text='')
      self.tree5.bind("<Double-Button-1>", selectItem3)
      # self.tree5.pack(side=LEFT,ipadx=100)
      self.tree5.grid(row=2,column=21,ipady=40,ipadx=10)
#       
#       #show the revision history
      self.tree6=ttk.Treeview(root,show="headings",columns=(0,1),height=15)
      self.tree6.column(0,width=40)
      self.tree6.heading(0,text="Commit")
      self.tree6.column(1,width=100)
      self.tree6.heading(1,text='Modified')
      # self.tree6.pack(side=LEFT,ipadx=100)
      self.tree6.grid(row=2,column=22,columnspan=2,ipady=40,ipadx=20)
      self.tree6.bind("<Double-Button-1>",restoreversion)
      
      self.e1 = Text(root,width=45)
      self.e1.grid(row=1,column=21,columnspan=2,ipadx=5)

#       
#       #check version
#       self.button3=Button(self,text="VERSION")
#       # self.button3.pack(ipadx=15,side=LEFT)
#       self.button3.grid(row=3,column=1,ipadx=15)
#       self.button3.bind("<ButtonRelease-1>",commit1)
#       
#       #commit file
#       self.button4=Button(self,text="Commit")
#       # self.button4.pack(ipadx=15,side=LEFT)
#       self.button4.grid(row=3,column=2,ipadx=15)
#       self.button4.bind("<ButtonRelease-1>",commit_v)
#       
#       #show the branches
#       self.button5=Button(self,text="branch")
#       # self.button5.pack(ipadx=15,side=LEFT)
#       self.button5.grid(ipadx=15,row=3,column=3)
#       self.button5.bind("<ButtonRelease-1>",branch)
#       self.button5.bind("<Button-1>",clear_all2)      
# 
#       #show the revision history
#       self.button6=Button(self,text="Revision History")
#       # self.button6.pack(ipadx=15,side=LEFT)
#       self.button6.grid(ipadx=15,row=3,column=4)
#       self.button6.bind("<ButtonRelease-1>",revision)
#       self.button6.bind("<Button-1>",clear_all4)      


  def  print11(self):
       if self.valueputin.get() !="":
          self.valueInput=self.valueputin.get()
       elif self.valueputin.get()=="":
          self.valueInput=filedialog.askdirectory()
          print (self.valueInput)

       # self.valueInput=filedialog.askdirectory()

       keyvalue=self.valueInput
       cmd1=r'git config --global core.quotepath false'
       cmd2=r'git status'
 
       cmd=cmd1 +"&&" +cmd2
       print(keyvalue)
       cmdpath=str(keyvalue)
 
       process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
 
       stdout=process.communicate()
 
       process.wait()
       result=process.returncode
       aaa=type(stdout)
       vv=stdout[0]
       aa=str(vv,'utf-8')
 
       print(str(vv,'utf-8'))
 
       L=aa.split('\n')
       #insert UNTRACKED FILES
       if aa.find('Untracked files:')>=0:
         countu=L.index('Untracked files:')
         print(L.index('Untracked files:'))
         L=L[countu+3:-3]
         L2=[x.replace('\t','') for x in L]
         for i in L2:
           print(i)
           self.tree.insert("","end",values=(i))
           print(L2)

       #insert deleted files
       L3=aa.split('\n')
       print(L3)
       for item in L3:
         if item.find('deleted')>=0:
           # countd=L3.index('\tdeleted')

           item=item.split(":")[1]
           self.tree3.insert("","end",values=(item))
           print(item)
           
       L4=aa.split('\n')
       print(L4)
       for item in L4:
         if item.find('modified')>=0:
           # countd=L3.index('\tdeleted')

           item=item.split(":")[1]
           self.tree3_2.insert("","end",values=(item))
           print(item)
       
       self.T.config(state=NORMAL)
       self.T.insert(END,aa)
       self.T.config(state=DISABLED)
       

       
       
       def selectItem(a):
           curItem=self.tree.focus()
           zz=self.tree.item(curItem)["values"]
           print(zz)
           if zz != "":
             self.tree2.insert("","end",values=(zz))
             self.tree.delete(curItem)
 #          print(tree.identify_row(a))
           #输出选中值的特性
       
       self.tree.bind("<ButtonRelease-1>", selectItem)
       
       def selectItem2(a):
           curItem=self.tree2.focus()
           zz=self.tree2.item(curItem)["values"]
           if zz != "":
             print(zz)
             self.tree.insert("","end",values=(zz))
             self.tree2.delete(curItem)
             
       #restore deleted files
       
       def restorefile(a):
           curItem=self.tree3.focus()
           msg=messagebox.askquestion(title="Restore",message="Restore the file?")
           if msg=='yes':
#             print(self.valueInput.get())
             keyvalue=self.valueInput
             zz=self.tree3.item(curItem)["values"]
             print(self.tree3.item(curItem)["values"])
             self.tree3.delete(curItem)
             z=zz[0]
             cmd=r'git checkout '
             cmd=cmd+z
             process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)

             stdout=process.communicate()
   
             process.wait()
             result=process.returncode

#add modified files
      
       def add_modify(a):
           global z


           self.e1.delete(1.0,END)


          #  self.filemenu2=Menu(self.menubar,tearoff=0)
          # 
          #  self.filemenu2.add_command(label="Restore",command=restore_temp)   
          #  self.filemenu2.add_command(label="Add",command=add_temp)
          #  self.menubar.add_cascade(label="Modified",menu=self.filemenu2)
           
           curItem=self.tree3_2.focus()
           
           zz=self.tree3_2.item(curItem)["values"]
           if zz != "":

            msg=messagebox.askquestion(title="Restore modify",message="Restore modified file?")
            if msg=='yes':
            # print(self.valueInput.get())
              keyvalue=self.valueInput 
              zz=self.tree3_2.item(curItem)["values"]
              print(self.tree3_2.item(curItem)["values"])
              self.tree3_2.delete(curItem)
              z=zz[0]
              print(z)



              # cmd0=r'git config --global core.editor "C:/cygwin/bin/"'
              cmd1=r'git config --global diff.tool p4merge'
              cmd2=r'git config --global difftool.prompt false'
              cmd3=r'git config --global alias.d difftool'
              cmd4_1=r'git d '
              cmd4=cmd4_1+z
              cmd5=cmd1+"&&"+ cmd2+"&&"+ cmd3+"&&"+cmd4
              process=subprocess.Popen(cmd5,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
              stdout1=process.communicate()
              process.wait()
              result=process.returncode
              
              cmd=r'git diff '
              cmd=cmd+z
              cmd5=cmd 
              process=subprocess.Popen(cmd5,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
              stdout=process.communicate()
              process.wait()
              result=process.returncode

              print(stdout)
              vv1=stdout[0]
              print(vv1)
              aa1=vv1.decode('cp936')
              print(aa1)
              stdout=str(stdout)

              stdout=stdout[3:-8]
              print(stdout)
              L=aa1.split('\n')
              L=np.array(L)
              L=L.reshape(-1,1)
              L=pd.DataFrame(L)
              print(L)
              count=1
              for i in L.index:
                  a=L.loc[i][0]+"\n"
                  print(a)
                  print(str(count)+".0")
                  if a.find('+')!=-1:
                    print(count)

                    self.e1.insert(INSERT,a)
                    self.e1.tag_add("here",str(count)+".0",str(count)+".50")
                    self.e1.tag_config("here",foreground="red")
                    
                  else:
                    self.e1.insert(INSERT,a)
                  count+=1
              return z
              return zz   


              #     top.destroy()
              #     
              # top = Toplevel()
              # top.title('Different from last Commit Version')

              # v1 = StringVar()
              # buttonc=Button(top,text="Restore")
              # buttonc.grid(row=0,column=0,padx=10,pady=10)
              # buttonc.bind("<ButtonRelease-1>",restore_temp) 
              # buttonadd=Button(top,text="Add to commit")
              # buttonadd.grid(row=0,column=2,padx=10,pady=10)
              # buttonadd.bind("<ButtonRelease-1>",add_temp)   
              # e1 = Text(top,width=100,height=100)
              # e1.grid(row=1,column=1,padx=100,pady=100)

              
#               cmd=r'git checkout '
#               cmd=cmd+z
#               process=subprocess.Popen(cmd,shell=True,cwd=cmdpath,stdout=subprocess.PIPE)
# 
#               stdout=process.communicate()
#     
#               process.wait()
#               result=process.returncode
                
               

     
 

       #button binding
       self.tree2.bind("<ButtonRelease-1>", selectItem2)
       
       self.tree3.bind("<ButtonRelease-1>",restorefile)

       self.tree3_2.bind("<Double-Button-1>",add_modify)



 

#  
# def callback():
#     messagebox.showwarning('警告','回答问题')


root=Tk()
root.geometry('1300x700')

app=untrack()
root.title("Git GUI")

# root.protocol("hhh",callback)

root.mainloop()





 
 









