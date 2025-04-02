<script>
export default {
  props: {
    question: Object,
    questionnaireId: Number,
  },
  methods: {
    suppr() {
      const requete = `http://127.0.0.1:5000/quiz/api/v1.0/questionnaire/${this.questionnaireId}/question/${this.question.idQuestion}`;
      
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
        this.$emit('remove', this.question.idQuestion);
      })
      .catch(error => {
        console.error(error);
      });
    }
  },
  emits: ['remove']
}
</script>

<template>
  <button @click="suppr">X</button>
</template>

<style scoped>
.btn {
  margin-left: 10px;
}
</style>