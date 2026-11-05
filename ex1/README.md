1. "" dá {} - Este é o teste mais simples, pois não contém nenhuma palavra, resultando em um dicionário vazio.
2. "teste" dá {"teste": 1} - Este teste é simples, pois contém apenas uma palavra, permitindo verificar se o contador de palavras funciona corretamente para casos básicos.
3. "Dia dia DIA" dá {"dia": 3}
4. "fim. Fim!" dá {"fim": 2}
5. "dia a dia" dá {"dia": 2}
6. "bom dia" dá dois itens
7. "bom\ndia" dá dois itens
8. "guarda-chuva" dá um item
9. ",dia, ;dia;" dá {"dia": 2}
10. ":dia: ?dia?" dá {"dia": 2}
11. Três espaços entre bom e dia dão dois itens

b) verificar commits desse repositório

c) nenhum GREEN veio sem RED antes
```
⟩ git log --oneline
50ceed3 (HEAD -> main) ex1 REFACTOR tres espacos
d9c64bd ex1 GREEN tres espacos
effeb90 erro de digitacao
bfed6ed ex1 RED tres espacos
932e9e7 ex1 REFACTOR hifen
3126e89 ex1 GREEN hifen
3472fde ex1 RED hifen
c758d8d ex1 REFACTOR pontos
342ca23 ex1 GREEN pontos
e17ce7f ex1 RED pontos
e97fc92 ex1 REFACTOR cases
88e4b12 ex1 GREEN cases
d0c130c ex1 RED cases
c4d2313 ex1 GREEN
1569019 ex1 RED
da6a050 gitignores
5b56a24 pyproject.toml
6a0618b add mutants
b32c2d7 (origin/main, origin/HEAD) Initial commit
```

d) a maior parte dos testes passaram na primeira execução (5, 6, 7, 9, 10). O código já estava correto para esses casos, mas falhou em outros.

e) 23 mutantes gerados, 22 mortos, 1 ignorado.
