<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';
import QuestionnaireItem from './components/questionnaireItem.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: ''
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
    }
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  },
  components: { QuestionnaireItem, AjouterQuestionnaire }
}
</script>

<template>
  <h1>Hello</h1>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q">
    </QuestionnaireItem>
   </li>
       <AjouterQuestionnaire @add="addQuestionnaire"/>

</template>


