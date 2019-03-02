import hudson.plugins.git.*;

def scm = new GitSCM("git@github.com:sumedhbala/InfraTest.git")
scm.branches = [new BranchSpec("*/developer")];

def flowDefinition = new org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition(scm, "jenkins/jobs/try.groovy")

def parent = Jenkins.instance
def job = new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent, "New Job")
job.definition = flowDefinition

parent.reload()
