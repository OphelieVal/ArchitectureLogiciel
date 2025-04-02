<script>
  export default {
    props: {
      question: Object,
      questionnaireId: Number,
    },
    methods: {
      suppr : function() {
        this.$emit('remove', {idQuestion: this.question.idQuestion});
      }
    },
    emits : ['remove']
  }
</script>

<template>
  <button class="btn btn-default" @click="suppr">X</button>
</template>

<style scoped>
.btn {
  margin-left: 10px;
}
</style>