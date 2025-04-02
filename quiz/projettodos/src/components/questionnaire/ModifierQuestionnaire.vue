<script>
export default{
    props: {
        questionnaire : Object
    },
    data() {
        return {
            nvQuestionnaire: this.questionnaire.name
        };
    },
    methods : {
        update: function() {
            this.$emit('update', {  id: this.questionnaire.id, name: this.nvQuestionnaire });
        }
    },
    emits : ['update'],
};
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
*    <input id="modifierQuestionnaire" v-model="nvQuestionnaire"
        @keyup.enter="update" 
        placeholder="Entrer le nouveau nom"
        type="text"
        class="form-control">
    <button class="btn btn-dark" @click="update">Enregistrer</button>
</template>
