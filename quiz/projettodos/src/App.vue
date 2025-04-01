<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';
import ModifierQuestionnaire from './components/ModifierQuestionnaire.vue';
import QuestionnaireItem from './components/questionnaireItem.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: '',
  modifQuestionnaire: null
}

export default {
  data(){
    return data;
  },
  methods: {
    addQuestionnaire(name) {
      if (name) {
      const requete = "http://127.0.0.1:5000/quiz/api/v1.0/questionnaire";
      fetch(requete, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: name }),
      })
      .then(response => {
                  if (response.ok) return response.json();
                  else throw new Error('Problème ajax: '+response.status);
                }
            )
      .then(data => {
        this.questionnaires.push(data.questionnaire);
      })
      .catch(error => {
        console.error(error);
      });
      }
    },
    updateQuestionnaire() {
      if (this.modifQuestionnaire) {
        const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${this.modifQuestionnaire.id}`;
        fetch(requete, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: this.modifQuestionnaire.name }),
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Problème ajax: ' + response.status);
          }
          return response.json();
        })
        .then(data => {
          const index = this.questionnaires.findIndex(q => q.id === data.id);
          this.questionnaires[index] = data;
          this.modifQuestionnaire = null;
        })
        .catch(error => {
          console.error('Erreur lors de la modification du questionnaire :', error);
        });
      }
    } 
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  },
  components: { QuestionnaireItem, AjouterQuestionnaire, ModifierQuestionnaire }
}
</script>

<template>
  <h1>Hello</h1>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q"/>
    <button @update="updateQuestionnaire(q)">Modifier</button>
   </li>
    <AjouterQuestionnaire @add="addQuestionnaire"/>

    <div v-if="modifQuestionnaire">
      <input v-model="modifQuestionnaire.name" placeholder="Nom du questionnaire"/>
      <button @update="updateQuestionnaire">Enregistrer</button>
    </div>
</template>


