from application import db


class Genes(db.Model):
    '''
        Python/SQL Alchemy definition for databse table.
    '''
    
    __tablename__ = 'gene_autocomplete'         # Database table name
    __table_args__ = {'extend_existing': True}  # This is an existing table. Do not create.
    
    # Table fields
    species = db.Column(db.String(255))
    display_label = db.Column(db.String(128))
    stable_id = db.Column(db.String(128), primary_key=True)
    location = db.Column(db.String(60))

    def __repr__(self):
        return '<Gene {}>'.format(self.display_label)
