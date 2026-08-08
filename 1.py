#started apache spark
"""
Python
      ↓
Python Practice
      ↓
Apache Spark Concepts
      ↓
PySpark
      ↓
Databricks
      ↓
Delta Lake
      ↓
Spark Optimization
      ↓
Projects
      ↓
Interviews
"""



# multiple machines to process big data  and compile into final part
# 1 create spark session

# create driver 
# worker 
#executor

#cluster manaeger finds worker 

# after creating session 
# data logic

# resource manager is master
# resources in form of dricers and workers 
# cluster is driver + worker 


# we can use databricks
# if using databricks its good
# to handle big data there are 2 ways : monolithic  second is distributed 
#in monolithic: we upgrade a machine ..like adding ram storage etc
#distibuted: apache spark it is : there is limit on monolithic instead of upgreading add more machines called as  horizontal scaling
# has higher availablity 

# spark vs mapReduce : 

# master- slave architecture

#we submit code to resource manager 
# ex  1 driveer of 10 gb   3 executors 20 gb each info will be provded by person it is spark submit 
# this will go to manager it creates driver node this driver is connected to manager drriver will take the request
#and it send the req back and tell to create executors on machines
#now driver takes cares of the workers in himself that is it is now conenected to the workers , it distributes the job to workers nodes
#driver node orchestrates the work


# our code goes to manager it creates driver program , manager creates worker nodes-they are machines...executors are different.
# 1 worker has 1 executor
# worker are connected to driver program 
# spark context is now spark session. its the starting point
# we connect driver to manager via spark context or session
#it sets up the connection
# manager creates app master container 
# pyspark ---> jvm main
# spark has java wrapper then it has python wrapper 
 # worker node has jvm 

#databrics helps us to worl with spark


#spark creates a dag for a job
#dag is directed acyclic graph
#ai please explain this

