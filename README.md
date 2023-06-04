# Sistema de Comunicação Pub-Sub usando Sockets em Python
- Este projeto implementa um sistema de comunicação baseado em publicação e assinatura (Publish-Subscribe) em Python. Ele permite que os clientes publiquem mensagens em diferentes tópicos e que os clientes assinem tópicos específicos para receber as mensagens correspondentes.

## Funcionalidades
Cliente Assinante: O código fornece uma função run_client_subscriber(topic) que representa um cliente assinante. Ele se conecta a um servidor de assinatura, inscreve-se em um tópico específico e recebe todas as mensagens publicadas nesse tópico.

Cliente Publicador: Os clientes publicadores podem se conectar ao servidor de publicadores e enviar mensagens para um determinado tópico. O servidor encaminha essas mensagens para todos os clientes assinantes que estão inscritos no mesmo tópico.

Servidor: O servidor é responsável por gerenciar a comunicação entre os clientes publicadores e assinantes. Ele executa duas tarefas em paralelo:

Servidor de Publicadores: Aceita conexões de clientes publicadores, recebe as mensagens enviadas por eles e encaminha essas mensagens para os assinantes apropriados. <br><br>
Servidor de Assinantes: Aceita conexões de clientes assinantes, recebe os comandos de inscrição e cancelamento de inscrição em tópicos e envia as mensagens publicadas anteriormente aos assinantes recém-conectados. <br><br>
Bloqueio de Acesso Compartilhado: O código utiliza objetos Lock para garantir que os dados compartilhados entre as threads sejam acessados de forma segura. Isso evita conflitos de acesso concorrente aos tópicos, assinantes e mensagens. <br>

## Uso
- Clone o repositório para sua máquina local.
- Certifique-se de ter o Python instalado (versão 3+).
- Abra um terminal e navegue até o diretório clonado.
- Execute o servidor executando o seguinte comando: python server.py.
- Em outro terminal, execute um ou mais clientes publicadores usando o seguinte comando: python client_publisher.py.
- Em outro terminal, execute um ou mais clientes assinantes usando o seguinte comando: python client_subscriber.py.
- Siga as instruções exibidas na saída para publicar mensagens e assinar tópicos.
Certifique-se de ajustar os endereços IP e as portas, se necessário, nos códigos do servidor e dos clientes para corresponder às suas configurações de rede.

## Desenvolvimento
Este projeto foi desenvolvido como uma demonstração de um sistema de comunicação Pub-Sub usando sockets em Python como forma de avaliação da disciplina de Redes de Computadores da UNICAP.
