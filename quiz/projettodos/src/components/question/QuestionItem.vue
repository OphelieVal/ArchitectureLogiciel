<script>
export default{
    props: {
        question : Object
    }
}
</script>
<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
      <div v-bind:class="{question}">
        <p v-bind="question"> {{ question.title }}</p>
      </div>
</template>