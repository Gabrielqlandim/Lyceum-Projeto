describe('historia de filtrar aluno', () => {
    let nome = "teste";
    let senha = "123";

    it('filtrar alunos por nome em ordem alfabetica com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();

        cy.get('tbody > :nth-child(1) > :nth-child(2)').invoke('text').as('name_first');

        cy.wait(2000); 
        cy.get('[onclick="sort(1)"]').click();
        cy.wait(2000);
        cy.get('[onclick="sort(1)"]').click();
        cy.wait(2000);

        cy.get('@name_first').then((name_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(2)').should('have.text', name_first);
        });
    })
    it('filtrar alunos por serie/turma com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();

        cy.get('tbody > :nth-child(1) > :nth-child(3)').invoke('text').as('class_first');

        cy.wait(2000); 
        cy.get('[onclick="sort(2)"]').click();
        cy.wait(2000); 
        cy.get('[onclick="sort(2)"]').click();
        cy.wait(2000);

        cy.get('@class_first').then((class_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(3)').should('have.text', class_first);
        });
    })
    it('filtrar alunos por data de matricula com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();

        cy.get('tbody > :nth-child(1) > :nth-child(4)').invoke('text').as('date_first');

        cy.wait(2000); 
        cy.get('[onclick="sort(3)"]').click();
        cy.wait(2000);
        cy.get('[onclick="sort(3)"]').click();
        cy.wait(2000);

        cy.get('@date_first').then((date_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(4)').should('have.text', date_first);
        });
    })       
    it('filtrar alunos por id com sucesso', () => {
        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
        cy.get('#aalunos').click();

        cy.get('tbody > :nth-child(1) > :nth-child(1)').invoke('text').as('id_first');


        cy.wait(2000); 
        cy.get('[onclick="sort(0)"]').click();
        cy.wait(2000);  
        cy.get('[onclick="sort(0)"]').click();
        cy.wait(2000);

        cy.get('@id_first').then((id_first) => {
            cy.get('tbody > :nth-child(1) > :nth-child(1)').should('have.text', id_first);
        });
    })                                
})          