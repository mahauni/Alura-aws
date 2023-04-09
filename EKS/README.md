# EKS

### Configuring Dev Workspace

EKS is under it is a instance of EC2 with kubectl, minikube and Docker running in the backgroud, so you will need install both in the EC2 you have.

Minikube is a developer tool, and not to take it to production. To use kubernetes in production you will need to create the whole infraestucture to use the kubernetes, so create pods, a pod master, etc.

### EC2 connection to the outside.

Most aplications will need to connect to the outside world or to other clusters, aplications, services.
And for that you will need to change the IAM policy to you need and security groups.

### Configuring a Prodution Workspace

You will need to have AWS CLI and at least the 1.16.73 version because it has EKS commands.
Create a IAM to have the access to the EKS if you are not root user. But is always usefull to have it already there.
Its good to create a VPC to the EKS to separate the cluster.

### EKS cluster cli commands

Create a EKS cluster
```bash
$ aws eks create-cluster --name [name] --role-arn [IAM role] --resources-vpc-config subnetIds=[ids1], [ids2], security GroupIds=[security group]
```

List all EKS clusters
```bash
$ aws eks list-clusters
```

Describe the named cluster

```bash
$ aws eks describe-cluster --name [cluster name]
```

### Management of clusters

We will use the kubectl to manage the clustes.
To manage with the kubectl, you will need to have a updated version of kubectl that is compatible with the file of AWS.
First install the aws-iam-autenticator for kubectl in the AWS website.

After installing the aws-iam-autenticator, and moving to the PATH. Update the eks cluster with the:

```bash
$ aws eks update-kubeconfig --name [cluster name]
```

and to verify if is done everything allright, you should be able to do the command and the cluster of aws will appear:

```bash
$ kubectl get svc
```

### Creating nodes

Create nodes to for our EKS. Instead of creating all nodes by hand, auto-scaling, vpc and all the stuff. Use CloudFormation, and use the template the AWS provide to create some nodes.
Add all the information, the vpc and its subnets the EKS is in, the intances of EC2, the amount of intances, max, min, desirable.
You can change the amount of the load-balancer of instances inside the CloudFormation.

### Linking the EC2 instances with the EKS

For this we will be usign the kubectl.
For this we will go to the AWS web page and go to the part where they talk about linking nodes to EKS.
There you will upload a aws-auth.yaml file. And then you will need to edit the rolearn part.
The rolearn part you will find, if you are using CloudFormation, If you click in the EC2 stack we created, there will be a outputs dropdown bar, and then you will find the NodeInstanceRole. And the NodeIntanceRole Value is where we will copy and paste in the place of the rolearn.
After editing the file and saving you will apply this config with

```bash
$ kubectl apply -f aws-auth.yaml
```

and if you check the nodes, you will be able to see the nodes there.

### Deploying the Prodution Cluster.

In our test cluster, we used only one instance of EC2 and the clusters where linked to the external world via NodePortl but this is mostly a Dev thing.
In the Production we will use a load balancer to connect to the outside world, and this is mostly the difference between the Prod and the Dev one.
The file of the production and the things you need to do to upload are in the example_eks.sh

### Escaling the Cluster.

To scale to more nodes in the cluster, you can go to the CloudFormation stack of nodes and increase the size of the nodes.
The nodes will be automaticaly put in the EKS cluster the stack is in, because of previous settings.

If you want to increase the pods, you can scale with the command

```bash
$ kubectl scale deploy [name of pods] --replica=[n of replicas]
```

like normal kubectl. So to scale pods, is normal like you are using the kubectl minikube etc to scale.


### Kubernetes Dashboard

In the kubernetes website, it has some instructions on how to set it up the dashboard and all the instructions on how to do it.

And this is a way on how to monitor you aplication. You can use others one, but the Alura shown the kubernetes one.