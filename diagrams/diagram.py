# mingrammer diagram as code for this template
# see https://diagrams.mingrammer.com/docs/nodes/aws

from diagrams import Cluster,Diagram
from diagrams.aws.network import VPC
from diagrams.aws.network import PrivateSubnet

with Diagram("Basic Networking"):
  svpc = VPC ("SimpleVPC")
  ssubnet = PrivateSubnet ("SimplePrivateSubnet")
  svpc >> ssubnet
