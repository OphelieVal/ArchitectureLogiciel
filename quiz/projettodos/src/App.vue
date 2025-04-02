<script>

import AjouterQuestionnaire from './components/AjouterQuestionnaire.vue';
import ModifierQuestionnaire from './components/ModifierQuestionnaire.vue';
import QuestionItem from './components/QuestionItem.vue';
import QuestionnaireItem from './components/questionnaireItem.vue';
import SupprQuestionnaire from './components/SupprQuestionnaire.vue';

let data = {
  questionnaires: [{id: 0, name: "hello"},{id: 1, name: "questionnaire"}],
  newQuestionnaire: '',
  modifQuestionnaire: null,
  questions: []
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
    updateQuestionnaire(nvQuest) {
      if (nvQuest) {
        const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${nvQuest.id}`;
        fetch(requete, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ name: nvQuest.name }),
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
          console.error(error);
        });
      }
    },
    getQuestions(id) {
      if (id) {
      const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${id}/question`;
      fetch(requete, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then(response => {
        if (response.ok) return response.json();
          else throw new Error('Problème ajax: '+response.status);
        }
      )
      .then(data => {
        console.log(data)
        this.questions = data
      })
      .catch(error => {
        console.error(error);
      });
      }
    },
    get_by_id: function(id) {
        for (let i = 0; i < this.questionnaires.length; i++) {
          if (this.questionnaires[i].id == id) {
            return this.questionnaires[i];
          }
        }
        return null;
      },
      remove_questionnaire(event) {
        if (event) {
          const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${event.id}`;
          
          fetch(requete, {
            method: 'DELETE',
            headers: {
              'Content-Type': 'application/json',
            },
          })
          .then(response => {
            if (!response.ok) {
              throw new Error('Problème ajax: ' + response.status);
            }
            return response.json();
          })
          .then(() => {
            this.questionnaires = this.questionnaires.filter(q => q.id !== event.id);
          })
          .catch(error => {
            console.error(error);
          });
        }
      },
    mounted(){
      fetch('http://localhost:5000/quiz/api/v1.0/questionnaire')
      .then(response => response.json())
      .then(json => {
        this.questionnaires = json
      })
    },
  },
  components: { QuestionnaireItem, AjouterQuestionnaire, ModifierQuestionnaire, QuestionItem, SupprQuestionnaire}
}
</script>

<template>
  <h1>QUIZ</h1>
  <li v-for="q of questionnaires" :questionnaire="q">
    <QuestionnaireItem :questionnaire="q"/>
    <SupprQuestionnaire :questionnaire="q" @remove="remove_questionnaire($event)" />
    <button @click="modifQuestionnaire=q">Modifier</button>
    <button @click="getQuestions(q.id)">voir les questions</button>

   </li>
    <AjouterQuestionnaire @add="addQuestionnaire"/>

    <ModifierQuestionnaire 
      v-if="modifQuestionnaire" :questionnaire="modifQuestionnaire"
      @update="updateQuestionnaire"
    />
    
    <div v-if="questions">
      <li v-for="quest in questions" :question="quest.idQuestion">
        <QuestionItem :question="quest" />
      </li>
    </div>
</template>


