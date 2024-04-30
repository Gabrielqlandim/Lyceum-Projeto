describe('historia de filtrar aluno', () => {
    let nome = "teste";
    let senha = "123";

    it('filtrar alunos por nome em ordem alfabetica com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(1)"]').click();
        cy.wait(2000);
        cy.get('[onclick="sort(1)"]').click();
        cy.wait(2000);
    })
    it('filtrar alunos por serie/turma com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(2)"]').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(2)"]').click();
        cy.wait(2000);
    })
    it('filtrar alunos por data de matricula com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(3)"]').click();
        cy.wait(2000);
        cy.get('[onclick="sort(3)"]').click();
        cy.wait(2000);  
    })       
    it('filtrar alunos por id com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(0)"]').click();
        cy.wait(2000);  
        cy.get('[onclick="sort(0)"]').click();
        cy.wait(2000); 
    })                                
})          