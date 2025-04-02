<script>
    export default {
        props : {
            questionnaire : Object
        },
        methods: {
            suppr : function() {
                this.$emit('remove', {id:this.questionnaire.id});
            }
        },
        emits : ['remove']
    }
</script>
<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <div class="container">
          <input type="button" class="btn btn-danger" value="Supprimer" @click="suppr" >
    </div>
</template>