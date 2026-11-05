Lista de testes, fora de ordem
"Dia dia DIA" dá {"dia": 3} "" dá {}
"fim. Fim!" dá {"fim": 2} "teste" dá {"teste": 1}
Três espaços entre bom e dia dão dois
itens
"guarda-chuva" dá um item
"dia a dia" dá dia 2 e a 1 "... !" dá {}
"bom\ndia" dá dois itens "bom dia" dá dois itens
",dia, ;dia;" dá {"dia": 2} ":dia: ?dia?" dá {"dia": 2}
CC8550 • Simulação e Teste de Software 8 / 20
Contador de Palavras
x Exercício 1
Use a especificação e a lista de testes apresentadas.
a) Ordene a lista do teste mais simples ao mais exigente. Justifique as
duas primeiras posições.

a) testes do mais simples ao mais difícil:

1. "" dá {} - Este é o teste mais simples, pois não contém nenhuma palavra, resultando em um dicionário vazio.
2. "teste" dá {"teste": 1} - Este teste é simples, pois contém apenas uma palavra, permitindo verificar se o contador de palavras funciona corretamente para casos básicos.
3. "Dia dia DIA" dá {"dia": 3} - Este teste verifica a contagem de palavras repetidas e a sensibilidade a maiúsculas e minúsculas.
4. "fim. Fim!" dá {"fim": 2} - Este teste avalia a contagem de palavras com pontuação, garantindo que a pontuação não afete a contagem correta.
5. "dia a dia" dá {"dia": 2} - Este teste verifica a contagem de palavras repetidas em uma frase com palavras separadas por espaços.
6. "bom dia" dá dois itens - Este teste avalia a contagem de palavras em uma frase simples, garantindo que o espaço entre as palavras seja tratado corretamente.
7. "bom\ndia" dá dois itens - Este teste verifica a contagem de palavras em uma frase com uma quebra de linha, garantindo que a quebra de linha seja tratada como um espaço.
8. "guarda-chuva" dá um item - Este teste avalia a contagem de palavras compostas, garantindo que palavras com hífens sejam contadas corretamente.
9. ",dia, ;dia;" dá {"dia": 2} - Este teste verifica a contagem de palavras com pontuação ao redor, garantindo que a pontuação não afete a contagem correta.
10. ":dia: ?dia?" dá {"dia": 2} - Este teste avalia a contagem de palavras com pontuação ao redor, garantindo que a pontuação não afete a contagem correta.
11. Três espaços entre bom e dia dão dois itens - Este teste verifica a contagem de palavras em uma frase com múltiplos espaços, garantindo que os espaços extras não afetem a contagem correta

b) verificar commits desse repositório
