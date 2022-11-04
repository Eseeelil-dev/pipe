node('master') {
    stage('Launch all') {
        build 'tests/pytest-part-1'
        build 'tests/pytest-part-2'
    }
}
