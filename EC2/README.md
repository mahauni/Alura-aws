### security groups

são instancias (policies) que são inseridas em produtos da AWS que faz com que a instancia do produto possa tanto receber como enviar informações para fora. Seria como um firewall

### instancias pre configuradas

fast start - pre registered images selected from aws - simple things for example kernels, distros, red hat, etc

aws marketplace - images that can be either from aws or enterprises whom aws has knowledge and has aproval to have the images. The images can either be paid of can be free.

community - anyone can upload images so aws has no garantee of what is the quality.

### Ações - imagens e modelo

modelo - fazer uma blueprint das configurações de hardware do ec2
imagens - fazer uma blueprint das configuraçoes de software do ec2

### ip elasticos

mesmo quando desligando a maquina ec2 e o ip dinamico da maquina ec2 modificado, o mesmo acontece ao reiniciar a maquina, se voce attach um ip elastico no ec2, mesmo que o ip do ec2 mude voce ainda conseguira entrar no mesmo ip que voce configuro no ip elastico e attached no ec2. veja os preço para o ip elastico colocando no google: aws elastic ip pricing

### aws rds

banco de dados relacional da aws. tem diversos banco de dados que aws disponibiliza. olhar preços.
para conectar você pode ou deixar ela apenas para instancias dentro da aws no mesmo local e com as mesmas security groups ou você pode definir para serviços extrernos acessarem.
é possivel definir para que o banco de dados fique em uma regiao e ser acessado por outras regioes, mas ai seria necessario fazer a modificar a vpc tanto do banco de dados e como da instancia que requer conectar com o banco. "Acredito que precisa as duas terem a mesma security group to acess the database"

### load balancer

load balancer redireciona request apenas para target groups. 
load balancer apenas consegue redirecionar para uma vpc disponivel e nas sub redes marcadas.

### auto scaling

ela utiliza-se modelos para o auto escalamento.
o modelo não precisa do security group de acesso á web. pois o load balancer que agora ta com porta aberta para o mundo externo e ai o load balancer que esta dentro da aws acessa as instancias.
o auto scaling cria instancias na vpc que voce selecionou e apenas nas sub redes selecionadas.
o balanciamento de carga (load balancer) é opicional, porém se você esta usando load balancer na sua aplicação é necessario colocar o auto scaling no target group que esta o load balancer. O mesmo acontece para todas as outras opções.
o auto scaling tem suas proprias instancias. Então se você tiver instancias que estão rodando separadamente do auto scaling e estão no target group, elas não serão contadas no auto scaling.

AWS CLI

