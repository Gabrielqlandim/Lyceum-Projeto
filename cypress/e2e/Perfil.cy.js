describe('perfil', () => {
    let nome = "teste";
    let email = "teste@cesar.school";
    let senha = "123";
    let novo_nome = "Eduardo";
    let novo_email = "eduardo123@cesar.school";
    let nova_senha = "2345678"

    beforeEach(() => {
        cy.visit('/');
        cy.get('#cadastrar-btn').click();
        cy.get('#nome').type(nome);
        cy.get('#email').type(email);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();

        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(senha);
        cy.get('#botao').click();
    })
    
    it('atualizar nome', () => {
        cy.visit('/perfil/');
        cy.get('#nome-professor').clear();
        cy.get('#nome-professor').type(novo_nome);
        cy.get('.btn').click();

        cy.get('.user > :nth-child(1)').should('have.text', novo_nome);
        
        cy.get('#nome-professor').clear();
        cy.get('#nome-professor').type(nome);
        cy.get('.btn').click();
    })

    it('atualizar email', () => {
        cy.visit('/perfil/');
        cy.get('#email-professor').clear();
        cy.get('#email-professor').type(novo_email);
        cy.get('.btn').click();

        cy.get('.user > :nth-child(2)').should('have.text', novo_email);
    })

    it('atualizar nome e email', () => {
        cy.visit('/perfil/');
        cy.get('#nome-professor').clear();
        cy.get('#nome-professor').type(novo_nome);
        cy.get('#email-professor').clear();
        cy.get('#email-professor').type(novo_email);
        cy.get('.btn').click();

        cy.get('.user > :nth-child(1)').should('have.text', novo_nome);
        cy.get('.user > :nth-child(2)').should('have.text', novo_email);
        
        cy.get('#nome-professor').clear();
        cy.get('#nome-professor').type(nome);
        cy.get('.btn').click();
    })

    it('atualizar senha', () => {
        cy.visit('/perfil/');
        cy.get('#senha-professor').type(nova_senha);
        cy.get('.btn').click();
        cy.get('#botao').click();

        cy.visit('/');
        cy.get('#nome').type(nome);
        cy.get('#senha').type(nova_senha);
        cy.get('#botao').click();

        cy.visit('/perfil/');
        cy.get('.user > :nth-child(1)').should('have.text', nome);
    })


    afterEach(() => {
        cy.visit('/admin/');
        cy.get('#id_username').type("adm");
        cy.get('#id_password').type("123");
        cy.get('.submit-row > input').click(); 
        cy.get('.model-user > th > a').click();
        cy.get('#searchbar').type(nome);
        cy.get('#changelist-search > div > [type="submit"]').click();
        cy.get('.action-select').click();
        cy.get('select').select('Remover usuários selecionados');
        cy.get('.button').click();
        cy.get('div > [type="submit"]').click();
    })
})