<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}]
}

export default {
  data(){
    return data;
  },
  methods: {
    addQuestionnaire: function () {
      let text = this.newItem.trim();
      if (text) {
        this.todos.push({
          text: text,
          checked: false
        });
        this.newItem = '';
      }
    }
  },
  mounted(){
    fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
    .then(response => response.json())
    .then(json => {
      this.questionnaires = json
    })
  }
}
</script>

<template>
  <h1>Hello</h1>
  <li v-for="question in questionnaires"> 
    {{ question.name }} 
  <AjouterQuestionnaire>
      v-for="q of questionnaires" :questionnaire="q"
      @add="addQuestionnaire">
  </AjouterQuestionnaire>
  </li>
</template>


