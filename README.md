# Descrição do PROJETO
# Projeto 2: Ping-Pong baseado em UDP

Neste projeto, a equipe desenvolverá uma aplicação ping-pong, que possui lado cliente e
servidor. O lado cliente
(i) enviará uma mensagem ping simples ao servidor
(ii) receberá uma mensagem pong correspondente de volta do servidor e
(iii) determinará o atraso entre o momento em que o cliente enviou a mensagem
ping e recebeu a mensagem pong.
(iv) Exibirá na tela o valor do atraso de cada ping.
O atraso em questão é denominado tempo de viagem de ida e volta (round-trip time —
RTT). A funcionalidade oferecida pelo cliente e servidor é semelhante à fornecida pelo
programa ping padrão, disponível nos sistemas operacionais modernos. Porém, os
programas ping padrão usam o Internet Control Message Protocol (ICMP). Neste projeto, a
aplicação ping-pong será baseada no UDP, fora do padrão (porém simples!). O programa
ping deverá enviar N mensagens ping ao servidor de destino por meio do UDP, sendo N um

valor informado pelo usuário da aplicação. Para cada mensagem, o cliente deverá
determinar e imprimir o RTT quando a mensagem pong correspondente for retornada. Ao
final da impressão dos RTTS das N mensagens de ping, deverá se exibir as seguintes
estatísticas: RTT máximo, RTT mínimo e RTT médio. Como o UDP é um protocolo não
confiável, um pacote enviado pelo cliente ou servidor poderá ser perdido. Por esse motivo, o
cliente não poderá esperar indefinidamente por uma resposta a uma mensagem ping. Deste
modo, a equipe deve implementar que o cliente espere até 1 s por uma resposta do
servidor; caso nenhuma resposta for recebida, o cliente deverá considerar que o pacote foi
perdido e imprimir uma mensagem correspondente. Ao final da impressão das estatísticas
de tempo, a aplicação também deve exibir o número de mensagens enviadas e no de
respostas recebidas.
