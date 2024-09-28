function mostrarResultado() {
  // Coletar valores dos campos booleanos
  const hair = document.getElementById('hair').checked;
  const feathers = document.getElementById('feathers').checked;
  const eggs = document.getElementById('eggs').checked;
  const milk = document.getElementById('milk').checked;
  const airborne = document.getElementById('airborne').checked;
  const aquatic = document.getElementById('aquatic').checked;
  const predator = document.getElementById('predator').checked;
  const toothed = document.getElementById('toothed').checked;
  const backbone = document.getElementById('backbone').checked;
  const breathes = document.getElementById('breathes').checked;
  const venomous = document.getElementById('venomous').checked;
  const fins = document.getElementById('fins').checked;
  const tail = document.getElementById('tail').checked;
  const domestic = document.getElementById('domestic').checked;
  const catsize = document.getElementById('catsize').checked;

  // Coletar valor numérico do número de pernas
  const legs = document.getElementById('legs').value;

  // Montar o form para consulta
  const formData = new FormData();
  formData.append('hair', hair);
  formData.append('feathers', feathers);
  formData.append('eggs', eggs);
  formData.append('milk', milk);
  formData.append('airborne', airborne);
  formData.append('aquatic', aquatic);
  formData.append('predator', predator);
  formData.append('toothed', toothed);
  formData.append('backbone', backbone);
  formData.append('breathes', breathes);
  formData.append('venomous', venomous);
  formData.append('fins', fins);
  formData.append('tail', tail);
  formData.append('domestic', domestic);
  formData.append('catsize', catsize);
  formData.append('legs', legs);

  let url = 'http://127.0.0.1:5000/animal';

  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) =>
      response.json())
    .then((result) => {

      let resultadoFinal = animalTypeDescription(result.type);

      // Exibir resultado no campo de texto
      document.getElementById('resultado').value = resultadoFinal.trim();
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

function animalTypeDescription(resultType) {
  // Mapeamento de tipos para as descrições
  switch (resultType) {
    case 1:
      return "Tipo 1: Mamíferos (41 animais) - Porco-da-terra, antílope, urso, javali, búfalo, bezerro, porquinho-da-índia, guepardo, veado, golfinho, elefante, morcego frugívoro, girafa, menina, cabra, gorila, hamster, lebre, leopardo, leão, lince, vison, toupeira, mangusto, gambá, órix, ornitorrinco, furão, pônei, boto, puma, gato doméstico, guaxinim, rena, foca, leão-marinho, esquilo, morcego-vampiro, toupeira, wallaby, lobo.";
    case 2:
      return "Tipo 2: Aves (20 animais) - Galinha, corvo, pomba, pato, flamingo, gaivota, falcão, kiwi, cotovia, avestruz, periquito, pinguim, faisão, ema, andorinha-do-mar, skua, pardal, cisne, abutre, carriça.";
    case 3:
      return "Tipo 3: Répteis (5 animais) - Víbora, serpente-marinha, licranço, tartaruga, tuatara.";
    case 4:
      return "Tipo 4: Peixes (13 animais) - Robalo, carpa, bagre, cabeçudo, cação, haddock (peixe similar ao bacalhau), arenque, lúcio, piranha, cavalo-marinho, linguado, arraia, atum.";
    case 5:
      return "Tipo 5: Anfíbios (4 animais) - Rã, rã, tritão, sapo.";
    case 6:
      return "Tipo 6: Insetos (8 animais) - Pulga, mosquito, abelha, mosca doméstica, joaninha, mariposa, cupim, vespa.";
    case 7:
      return "Tipo 7: Invertebrados (10 animais) - Amêijoa, caranguejo, lagostim, lagosta, polvo, escorpião, vespa-do-mar, lesma, estrela-do-mar, verme.";
    default:
      return "Tipo desconhecido";
  }
}