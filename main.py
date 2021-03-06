from model import *
from access import *		# import useful accessors classes
from data import *				# import data classes
from analysis import *				# import useful analysis classes
from orchestration import *

def displayDataCollec(data_collec):
  for e in data_collec:
	e.display()

print "Running script: "+ __file__		# aadl models location?
						
print "Initializing modules..."

# initialize the model
model=Model()

# initialize the accessors according to the model type
if model.model_type=="aadl":
	accessors=AADL_accessors(model.directory)	# aadl accessors
elif model.model_type=="cpal":
	accessors=CPAL_accessors(model.directory)	# cpal accessors

# initialize the data model with the accessors 
# temporary: hardcoded data	
data_model=DataModel(accessors);		# data model with accessors

# initialize the analyses
analysis_list=[]
ll_context=ll_context()				# context analyses	
analysis_list.append([ll_context.__class__.__name__, ll_context]) 
srl_pcp_context=srl_pcp_context()
analysis_list.append([srl_pcp_context.__class__.__name__,srl_pcp_context])
cheddar_simu_context=cheddar_simu_context()
analysis_list.append([cheddar_simu_context.__class__.__name__,cheddar_simu_context])
ll_rm_test=ll_rm_test()				# analyses
analysis_list.append([ll_rm_test.__class__.__name__, ll_rm_test])
srl_rm_test=srl_rm_test()	
analysis_list.append([srl_rm_test.__class__.__name__, srl_rm_test])
cheddar_simu=cheddar_simu()
analysis_list.append([cheddar_simu.__class__.__name__, cheddar_simu])
rm_mast= classic_rm_MAST()			
analysis_list.append([rm_mast.__class__.__name__, rm_mast])
srl_pcp_test_th16=srl_pcp_test_th16()
analysis_list.append([srl_pcp_test_th16.__class__.__name__, srl_pcp_test_th16])
srl_pcp_test_cor17=srl_pcp_test_cor17()				
analysis_list.append([srl_pcp_test_cor17.__class__.__name__, srl_pcp_test_cor17])
srl_pcp_test_th18=srl_pcp_test_th18()	
analysis_list.append([srl_pcp_test_th18.__class__.__name__, srl_pcp_test_th18])
lss_sporadic_test=lss_sporadic_test()
analysis_list.append([lss_sporadic_test.__class__.__name__, lss_sporadic_test])
rts_periodic_npfp=rts_periodic_npfp()		
analysis_list.append([rts_periodic_npfp.__class__.__name__, rts_periodic_npfp])

print "Execute analyses..."

choice = raw_input("Select the analysis mode:\n         type 'a' for automated analysis (pathfinder and paparazzi models only) \n         type 'm' for manual analysis (select analyses)\n         type any other key for hardcoded process \n> ");

if choice=='a': 
	# execute analyses according to analysis graph

	print "Select the analysis goal: \n> isSchedulable (default choice)"
	goal="isSchedulable"

	# initializes orchestration module with analysis graph 
	# the analysis graph is hardcoded from Alloy module

	if 'pathfinder' in model.directory:
	   # dependency graph representing dependent tasks for mars pathfinder case study
	   accessors.dependency_graph={"T1": ["T2"],"T2": [],"T3": []}		# comment line for independent taskset / uncomment for dependent taskset

	   # analysis graph for the pathfinder case study
	   # caution: the graph can admit redundant paths (to improve?)
	   # caution: pre-analyses must me be placed before analyses (to improve)
	   analysis_graph = { 
		  	model.directory : [ll_context, srl_pcp_context, cheddar_simu_context, ll_rm_test, srl_rm_test, srl_pcp_test_th16, 				srl_pcp_test_cor17, srl_pcp_test_th18],
		  	ll_context : [ll_rm_test, srl_rm_test],
			srl_pcp_context : [srl_pcp_test_th16, srl_pcp_test_cor17, srl_pcp_test_th18],
			cheddar_simu_context : [cheddar_simu],
		  	ll_rm_test : [goal],
		  	srl_rm_test : [goal],
			cheddar_simu : [goal],
		  	srl_pcp_test_th16 : [goal],
			srl_pcp_test_cor17 : [goal],
		  	srl_pcp_test_th18 : [goal],
		  	goal : [],
		}
	elif 'paparazzi' in model.directory:
	    # analysis graph for the paparazzi drone
	    analysis_graph = { 
	  	model.directory : [ll_context, ll_rm_test, srl_rm_test, lss_sporadic_test],
	  	ll_context : [ll_rm_test, srl_rm_test],
	  	ll_rm_test : [goal],
	  	srl_rm_test : [goal],
		lss_sporadic_test : [goal],
	  	goal : [],
		}
	else: 
	    analysis_graph = None

	o = Orchestration(analysis_graph)

	# Visit the analysis graph 
    	if o.visit_graph(model.directory, goal, data_model)==True:
		print "'"+goal+"' is successful!"
	else: 
		print "'"+goal+"' is not successful..."

elif choice=='m':

	exec_list=[]
	i=0
	display=''
	for element in analysis_list:
		i+=1
		display+='('+str(i)+') '+element[0]+' ' 

	print 'Available analyses are: '+display+'\r\n'+'Select analyses to execute (type 0 to finish selection)'

	endloop=False
	while not endloop:
		choice = raw_input('> ');	 
		if int(choice)==0: 
			endloop=True
		else: 
			exec_list.append(analysis_list[int(choice)-1][1])

	for element in exec_list:
		element.analysis(data_model)

else: 
	# execute hardcoded analyses  
	print "Execute hardcoded analysis process..."			
#	srl_rm_test.analysis(data_model)
	ll_rm_test.analysis(data_model)
#	srl_pcp_context.analysis(data_model)			
	#srl_pcp_test_th16.analysis(data_model)			
	#srl_pcp_test_cor17.analysis(data_model)
	#srl_pcp_test_th18.analysis(data_model)				
	#rta.analysis(data_model)			
	#rta_post.analysis(data_model)			
	#rma_context.analysis(data_model)		
#	rm_mast.analysis(data_model)	
#	lss_sporadic_test.analysis(data_model)
#	rts_periodic_npfp.analysis(data_model)



#from modulefinder import ModuleFinder

#finder = ModuleFinder()
#finder.run_script('main.py')

#print 'Loaded modules:'
#for name, mod in finder.modules.iteritems():
#	if "analysis" in name and name != "analysis.meta_analysis" and name != "analysis.lib_context": 
#    		print '%s ' % mod,
