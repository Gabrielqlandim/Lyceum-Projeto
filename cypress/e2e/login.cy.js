describe('cadastro e login', () => {
    let nome = "teste";
    let email = "teste@cesar.school";
    let senha = "123";

    it('cadstro com sucesso', () => {
        cy.visit('/');
        cy.get('#cadastrar-btn').click();
        cy.get('#nome').type(nome);
        cy.get('#email').type(email);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
    })
    it('login com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
    })
})